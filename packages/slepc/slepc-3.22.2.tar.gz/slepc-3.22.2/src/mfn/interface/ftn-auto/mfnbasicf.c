#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* mfnbasic.c */
/* Fortran interface file */

/*
* This file was generated automatically by bfort from the C source
* file.  
 */

#ifdef PETSC_USE_POINTER_CONVERSION
#if defined(__cplusplus)
extern "C" { 
#endif 
extern void *PetscToPointer(void*);
extern int PetscFromPointer(void *);
extern void PetscRmPointer(void*);
#if defined(__cplusplus)
} 
#endif 

#else

#define PetscToPointer(a) (a ? *(PetscFortranAddr *)(a) : 0)
#define PetscFromPointer(a) (PetscFortranAddr)(a)
#define PetscRmPointer(a)
#endif

#include "slepcmfn.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfnview_ MFNVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfnview_ mfnview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfnviewfromoptions_ MFNVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfnviewfromoptions_ mfnviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfnconvergedreasonview_ MFNCONVERGEDREASONVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfnconvergedreasonview_ mfnconvergedreasonview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfnconvergedreasonviewfromoptions_ MFNCONVERGEDREASONVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfnconvergedreasonviewfromoptions_ mfnconvergedreasonviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfncreate_ MFNCREATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfncreate_ mfncreate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfnsettype_ MFNSETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfnsettype_ mfnsettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfngettype_ MFNGETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfngettype_ mfngettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfnreset_ MFNRESET
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfnreset_ mfnreset
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfndestroy_ MFNDESTROY
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfndestroy_ mfndestroy
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfnsetbv_ MFNSETBV
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfnsetbv_ mfnsetbv
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfngetbv_ MFNGETBV
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfngetbv_ mfngetbv
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfnsetfn_ MFNSETFN
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfnsetfn_ mfnsetfn
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define mfngetfn_ MFNGETFN
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define mfngetfn_ mfngetfn
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  mfnview_(MFN mfn,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
CHKFORTRANNULLOBJECT(viewer);
*ierr = MFNView(
	(MFN)PetscToPointer((mfn) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  mfnviewfromoptions_(MFN mfn,PetscObject obj, char name[], int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(mfn);
CHKFORTRANNULLOBJECT(obj);
/* insert Fortran-to-C conversion for name */
  FIXCHAR(name,cl0,_cltmp0);
*ierr = MFNViewFromOptions(
	(MFN)PetscToPointer((mfn) ),
	(PetscObject)PetscToPointer((obj) ),_cltmp0);
  FREECHAR(name,_cltmp0);
}
SLEPC_EXTERN void  mfnconvergedreasonview_(MFN mfn,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
CHKFORTRANNULLOBJECT(viewer);
*ierr = MFNConvergedReasonView(
	(MFN)PetscToPointer((mfn) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  mfnconvergedreasonviewfromoptions_(MFN mfn, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
*ierr = MFNConvergedReasonViewFromOptions(
	(MFN)PetscToPointer((mfn) ));
}
SLEPC_EXTERN void  mfncreate_(MPI_Fint * comm,MFN *outmfn, int *ierr)
{
PETSC_FORTRAN_OBJECT_CREATE(outmfn);
 PetscBool outmfn_null = !*(void**) outmfn ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(outmfn);
*ierr = MFNCreate(
	MPI_Comm_f2c(*(comm)),outmfn);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! outmfn_null && !*(void**) outmfn) * (void **) outmfn = (void *)-2;
}
SLEPC_EXTERN void  mfnsettype_(MFN mfn,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(mfn);
/* insert Fortran-to-C conversion for type */
  FIXCHAR(type,cl0,_cltmp0);
*ierr = MFNSetType(
	(MFN)PetscToPointer((mfn) ),_cltmp0);
  FREECHAR(type,_cltmp0);
}
SLEPC_EXTERN void  mfngettype_(MFN mfn,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(mfn);
*ierr = MFNGetType(
	(MFN)PetscToPointer((mfn) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for type */
*ierr = PetscStrncpy(type, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, type, cl0);
}
SLEPC_EXTERN void  mfnreset_(MFN mfn, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
*ierr = MFNReset(
	(MFN)PetscToPointer((mfn) ));
}
SLEPC_EXTERN void  mfndestroy_(MFN *mfn, int *ierr)
{
PETSC_FORTRAN_OBJECT_F_DESTROYED_TO_C_NULL(mfn);
 PetscBool mfn_null = !*(void**) mfn ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(mfn);
*ierr = MFNDestroy(mfn);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! mfn_null && !*(void**) mfn) * (void **) mfn = (void *)-2;
if (*ierr) return;
PETSC_FORTRAN_OBJECT_C_NULL_TO_F_DESTROYED(mfn);
 }
SLEPC_EXTERN void  mfnsetbv_(MFN mfn,BV bv, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
CHKFORTRANNULLOBJECT(bv);
*ierr = MFNSetBV(
	(MFN)PetscToPointer((mfn) ),
	(BV)PetscToPointer((bv) ));
}
SLEPC_EXTERN void  mfngetbv_(MFN mfn,BV *bv, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
PetscBool bv_null = !*(void**) bv ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(bv);
*ierr = MFNGetBV(
	(MFN)PetscToPointer((mfn) ),bv);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! bv_null && !*(void**) bv) * (void **) bv = (void *)-2;
}
SLEPC_EXTERN void  mfnsetfn_(MFN mfn,FN fn, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
CHKFORTRANNULLOBJECT(fn);
*ierr = MFNSetFN(
	(MFN)PetscToPointer((mfn) ),
	(FN)PetscToPointer((fn) ));
}
SLEPC_EXTERN void  mfngetfn_(MFN mfn,FN *fn, int *ierr)
{
CHKFORTRANNULLOBJECT(mfn);
PetscBool fn_null = !*(void**) fn ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(fn);
*ierr = MFNGetFN(
	(MFN)PetscToPointer((mfn) ),fn);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! fn_null && !*(void**) fn) * (void **) fn = (void *)-2;
}
#if defined(__cplusplus)
}
#endif
