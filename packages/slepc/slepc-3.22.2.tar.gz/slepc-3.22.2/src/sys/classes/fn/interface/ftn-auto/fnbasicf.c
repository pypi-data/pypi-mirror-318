#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* fnbasic.c */
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

#include "slepcfn.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fncreate_ FNCREATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fncreate_ fncreate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fnsetoptionsprefix_ FNSETOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fnsetoptionsprefix_ fnsetoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fnappendoptionsprefix_ FNAPPENDOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fnappendoptionsprefix_ fnappendoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fngetoptionsprefix_ FNGETOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fngetoptionsprefix_ fngetoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fnsettype_ FNSETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fnsettype_ fnsettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fngettype_ FNGETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fngettype_ fngettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fnsetscale_ FNSETSCALE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fnsetscale_ fnsetscale
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fngetscale_ FNGETSCALE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fngetscale_ fngetscale
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fnsetmethod_ FNSETMETHOD
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fnsetmethod_ fnsetmethod
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fngetmethod_ FNGETMETHOD
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fngetmethod_ fngetmethod
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fnsetparallel_ FNSETPARALLEL
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fnsetparallel_ fnsetparallel
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fngetparallel_ FNGETPARALLEL
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fngetparallel_ fngetparallel
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fnevaluatefunction_ FNEVALUATEFUNCTION
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fnevaluatefunction_ fnevaluatefunction
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fnevaluatederivative_ FNEVALUATEDERIVATIVE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fnevaluatederivative_ fnevaluatederivative
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fnevaluatefunctionmat_ FNEVALUATEFUNCTIONMAT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fnevaluatefunctionmat_ fnevaluatefunctionmat
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fnevaluatefunctionmatvec_ FNEVALUATEFUNCTIONMATVEC
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fnevaluatefunctionmatvec_ fnevaluatefunctionmatvec
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fnsetfromoptions_ FNSETFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fnsetfromoptions_ fnsetfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fnview_ FNVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fnview_ fnview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fnviewfromoptions_ FNVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fnviewfromoptions_ fnviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fnduplicate_ FNDUPLICATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fnduplicate_ fnduplicate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define fndestroy_ FNDESTROY
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define fndestroy_ fndestroy
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  fncreate_(MPI_Fint * comm,FN *newfn, int *ierr)
{
PETSC_FORTRAN_OBJECT_CREATE(newfn);
 PetscBool newfn_null = !*(void**) newfn ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(newfn);
*ierr = FNCreate(
	MPI_Comm_f2c(*(comm)),newfn);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! newfn_null && !*(void**) newfn) * (void **) newfn = (void *)-2;
}
SLEPC_EXTERN void  fnsetoptionsprefix_(FN fn, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(fn);
/* insert Fortran-to-C conversion for prefix */
  FIXCHAR(prefix,cl0,_cltmp0);
*ierr = FNSetOptionsPrefix(
	(FN)PetscToPointer((fn) ),_cltmp0);
  FREECHAR(prefix,_cltmp0);
}
SLEPC_EXTERN void  fnappendoptionsprefix_(FN fn, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(fn);
/* insert Fortran-to-C conversion for prefix */
  FIXCHAR(prefix,cl0,_cltmp0);
*ierr = FNAppendOptionsPrefix(
	(FN)PetscToPointer((fn) ),_cltmp0);
  FREECHAR(prefix,_cltmp0);
}
SLEPC_EXTERN void  fngetoptionsprefix_(FN fn, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(fn);
*ierr = FNGetOptionsPrefix(
	(FN)PetscToPointer((fn) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for prefix */
*ierr = PetscStrncpy(prefix, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, prefix, cl0);
}
SLEPC_EXTERN void  fnsettype_(FN fn,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(fn);
/* insert Fortran-to-C conversion for type */
  FIXCHAR(type,cl0,_cltmp0);
*ierr = FNSetType(
	(FN)PetscToPointer((fn) ),_cltmp0);
  FREECHAR(type,_cltmp0);
}
SLEPC_EXTERN void  fngettype_(FN fn,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(fn);
*ierr = FNGetType(
	(FN)PetscToPointer((fn) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for type */
*ierr = PetscStrncpy(type, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, type, cl0);
}
SLEPC_EXTERN void  fnsetscale_(FN fn,PetscScalar *alpha,PetscScalar *beta, int *ierr)
{
CHKFORTRANNULLOBJECT(fn);
*ierr = FNSetScale(
	(FN)PetscToPointer((fn) ),*alpha,*beta);
}
SLEPC_EXTERN void  fngetscale_(FN fn,PetscScalar *alpha,PetscScalar *beta, int *ierr)
{
CHKFORTRANNULLOBJECT(fn);
CHKFORTRANNULLSCALAR(alpha);
CHKFORTRANNULLSCALAR(beta);
*ierr = FNGetScale(
	(FN)PetscToPointer((fn) ),alpha,beta);
}
SLEPC_EXTERN void  fnsetmethod_(FN fn,PetscInt *meth, int *ierr)
{
CHKFORTRANNULLOBJECT(fn);
*ierr = FNSetMethod(
	(FN)PetscToPointer((fn) ),*meth);
}
SLEPC_EXTERN void  fngetmethod_(FN fn,PetscInt *meth, int *ierr)
{
CHKFORTRANNULLOBJECT(fn);
CHKFORTRANNULLINTEGER(meth);
*ierr = FNGetMethod(
	(FN)PetscToPointer((fn) ),meth);
}
SLEPC_EXTERN void  fnsetparallel_(FN fn,FNParallelType *pmode, int *ierr)
{
CHKFORTRANNULLOBJECT(fn);
*ierr = FNSetParallel(
	(FN)PetscToPointer((fn) ),*pmode);
}
SLEPC_EXTERN void  fngetparallel_(FN fn,FNParallelType *pmode, int *ierr)
{
CHKFORTRANNULLOBJECT(fn);
*ierr = FNGetParallel(
	(FN)PetscToPointer((fn) ),pmode);
}
SLEPC_EXTERN void  fnevaluatefunction_(FN fn,PetscScalar *x,PetscScalar *y, int *ierr)
{
CHKFORTRANNULLOBJECT(fn);
CHKFORTRANNULLSCALAR(y);
*ierr = FNEvaluateFunction(
	(FN)PetscToPointer((fn) ),*x,y);
}
SLEPC_EXTERN void  fnevaluatederivative_(FN fn,PetscScalar *x,PetscScalar *y, int *ierr)
{
CHKFORTRANNULLOBJECT(fn);
CHKFORTRANNULLSCALAR(y);
*ierr = FNEvaluateDerivative(
	(FN)PetscToPointer((fn) ),*x,y);
}
SLEPC_EXTERN void  fnevaluatefunctionmat_(FN fn,Mat A,Mat B, int *ierr)
{
CHKFORTRANNULLOBJECT(fn);
CHKFORTRANNULLOBJECT(A);
CHKFORTRANNULLOBJECT(B);
*ierr = FNEvaluateFunctionMat(
	(FN)PetscToPointer((fn) ),
	(Mat)PetscToPointer((A) ),
	(Mat)PetscToPointer((B) ));
}
SLEPC_EXTERN void  fnevaluatefunctionmatvec_(FN fn,Mat A,Vec v, int *ierr)
{
CHKFORTRANNULLOBJECT(fn);
CHKFORTRANNULLOBJECT(A);
CHKFORTRANNULLOBJECT(v);
*ierr = FNEvaluateFunctionMatVec(
	(FN)PetscToPointer((fn) ),
	(Mat)PetscToPointer((A) ),
	(Vec)PetscToPointer((v) ));
}
SLEPC_EXTERN void  fnsetfromoptions_(FN fn, int *ierr)
{
CHKFORTRANNULLOBJECT(fn);
*ierr = FNSetFromOptions(
	(FN)PetscToPointer((fn) ));
}
SLEPC_EXTERN void  fnview_(FN fn,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(fn);
CHKFORTRANNULLOBJECT(viewer);
*ierr = FNView(
	(FN)PetscToPointer((fn) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  fnviewfromoptions_(FN fn,PetscObject obj, char name[], int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(fn);
CHKFORTRANNULLOBJECT(obj);
/* insert Fortran-to-C conversion for name */
  FIXCHAR(name,cl0,_cltmp0);
*ierr = FNViewFromOptions(
	(FN)PetscToPointer((fn) ),
	(PetscObject)PetscToPointer((obj) ),_cltmp0);
  FREECHAR(name,_cltmp0);
}
SLEPC_EXTERN void  fnduplicate_(FN fn,MPI_Fint * comm,FN *newfn, int *ierr)
{
CHKFORTRANNULLOBJECT(fn);
PetscBool newfn_null = !*(void**) newfn ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(newfn);
*ierr = FNDuplicate(
	(FN)PetscToPointer((fn) ),
	MPI_Comm_f2c(*(comm)),newfn);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! newfn_null && !*(void**) newfn) * (void **) newfn = (void *)-2;
}
SLEPC_EXTERN void  fndestroy_(FN *fn, int *ierr)
{
PETSC_FORTRAN_OBJECT_F_DESTROYED_TO_C_NULL(fn);
 PetscBool fn_null = !*(void**) fn ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(fn);
*ierr = FNDestroy(fn);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! fn_null && !*(void**) fn) * (void **) fn = (void *)-2;
if (*ierr) return;
PETSC_FORTRAN_OBJECT_C_NULL_TO_F_DESTROYED(fn);
 }
#if defined(__cplusplus)
}
#endif
