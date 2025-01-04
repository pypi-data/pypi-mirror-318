#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* rgbasic.c */
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

#include "slepcrg.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rgcreate_ RGCREATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rgcreate_ rgcreate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rgsetoptionsprefix_ RGSETOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rgsetoptionsprefix_ rgsetoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rgappendoptionsprefix_ RGAPPENDOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rgappendoptionsprefix_ rgappendoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rggetoptionsprefix_ RGGETOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rggetoptionsprefix_ rggetoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rgsettype_ RGSETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rgsettype_ rgsettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rggettype_ RGGETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rggettype_ rggettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rgsetfromoptions_ RGSETFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rgsetfromoptions_ rgsetfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rgview_ RGVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rgview_ rgview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rgviewfromoptions_ RGVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rgviewfromoptions_ rgviewfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rgistrivial_ RGISTRIVIAL
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rgistrivial_ rgistrivial
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rgcheckinside_ RGCHECKINSIDE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rgcheckinside_ rgcheckinside
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rgisaxisymmetric_ RGISAXISYMMETRIC
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rgisaxisymmetric_ rgisaxisymmetric
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rgcanuseconjugates_ RGCANUSECONJUGATES
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rgcanuseconjugates_ rgcanuseconjugates
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rgcomputecontour_ RGCOMPUTECONTOUR
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rgcomputecontour_ rgcomputecontour
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rgcomputeboundingbox_ RGCOMPUTEBOUNDINGBOX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rgcomputeboundingbox_ rgcomputeboundingbox
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rgcomputequadrature_ RGCOMPUTEQUADRATURE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rgcomputequadrature_ rgcomputequadrature
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rgsetcomplement_ RGSETCOMPLEMENT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rgsetcomplement_ rgsetcomplement
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rggetcomplement_ RGGETCOMPLEMENT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rggetcomplement_ rggetcomplement
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rgsetscale_ RGSETSCALE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rgsetscale_ rgsetscale
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rggetscale_ RGGETSCALE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rggetscale_ rggetscale
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rgpushscale_ RGPUSHSCALE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rgpushscale_ rgpushscale
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rgpopscale_ RGPOPSCALE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rgpopscale_ rgpopscale
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define rgdestroy_ RGDESTROY
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define rgdestroy_ rgdestroy
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  rgcreate_(MPI_Fint * comm,RG *newrg, int *ierr)
{
PETSC_FORTRAN_OBJECT_CREATE(newrg);
 PetscBool newrg_null = !*(void**) newrg ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(newrg);
*ierr = RGCreate(
	MPI_Comm_f2c(*(comm)),newrg);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! newrg_null && !*(void**) newrg) * (void **) newrg = (void *)-2;
}
SLEPC_EXTERN void  rgsetoptionsprefix_(RG rg, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(rg);
/* insert Fortran-to-C conversion for prefix */
  FIXCHAR(prefix,cl0,_cltmp0);
*ierr = RGSetOptionsPrefix(
	(RG)PetscToPointer((rg) ),_cltmp0);
  FREECHAR(prefix,_cltmp0);
}
SLEPC_EXTERN void  rgappendoptionsprefix_(RG rg, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(rg);
/* insert Fortran-to-C conversion for prefix */
  FIXCHAR(prefix,cl0,_cltmp0);
*ierr = RGAppendOptionsPrefix(
	(RG)PetscToPointer((rg) ),_cltmp0);
  FREECHAR(prefix,_cltmp0);
}
SLEPC_EXTERN void  rggetoptionsprefix_(RG rg, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(rg);
*ierr = RGGetOptionsPrefix(
	(RG)PetscToPointer((rg) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for prefix */
*ierr = PetscStrncpy(prefix, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, prefix, cl0);
}
SLEPC_EXTERN void  rgsettype_(RG rg,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(rg);
/* insert Fortran-to-C conversion for type */
  FIXCHAR(type,cl0,_cltmp0);
*ierr = RGSetType(
	(RG)PetscToPointer((rg) ),_cltmp0);
  FREECHAR(type,_cltmp0);
}
SLEPC_EXTERN void  rggettype_(RG rg,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(rg);
*ierr = RGGetType(
	(RG)PetscToPointer((rg) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for type */
*ierr = PetscStrncpy(type, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, type, cl0);
}
SLEPC_EXTERN void  rgsetfromoptions_(RG rg, int *ierr)
{
CHKFORTRANNULLOBJECT(rg);
*ierr = RGSetFromOptions(
	(RG)PetscToPointer((rg) ));
}
SLEPC_EXTERN void  rgview_(RG rg,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(rg);
CHKFORTRANNULLOBJECT(viewer);
*ierr = RGView(
	(RG)PetscToPointer((rg) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  rgviewfromoptions_(RG rg,PetscObject obj, char name[], int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(rg);
CHKFORTRANNULLOBJECT(obj);
/* insert Fortran-to-C conversion for name */
  FIXCHAR(name,cl0,_cltmp0);
*ierr = RGViewFromOptions(
	(RG)PetscToPointer((rg) ),
	(PetscObject)PetscToPointer((obj) ),_cltmp0);
  FREECHAR(name,_cltmp0);
}
SLEPC_EXTERN void  rgistrivial_(RG rg,PetscBool *trivial, int *ierr)
{
CHKFORTRANNULLOBJECT(rg);
*ierr = RGIsTrivial(
	(RG)PetscToPointer((rg) ),trivial);
}
SLEPC_EXTERN void  rgcheckinside_(RG rg,PetscInt *n,PetscScalar *ar,PetscScalar *ai,PetscInt *inside, int *ierr)
{
CHKFORTRANNULLOBJECT(rg);
CHKFORTRANNULLSCALAR(ar);
CHKFORTRANNULLSCALAR(ai);
CHKFORTRANNULLINTEGER(inside);
*ierr = RGCheckInside(
	(RG)PetscToPointer((rg) ),*n,ar,ai,inside);
}
SLEPC_EXTERN void  rgisaxisymmetric_(RG rg,PetscBool *vertical,PetscBool *symm, int *ierr)
{
CHKFORTRANNULLOBJECT(rg);
*ierr = RGIsAxisymmetric(
	(RG)PetscToPointer((rg) ),*vertical,symm);
}
SLEPC_EXTERN void  rgcanuseconjugates_(RG rg,PetscBool *realmats,PetscBool *useconj, int *ierr)
{
CHKFORTRANNULLOBJECT(rg);
*ierr = RGCanUseConjugates(
	(RG)PetscToPointer((rg) ),*realmats,useconj);
}
SLEPC_EXTERN void  rgcomputecontour_(RG rg,PetscInt *n,PetscScalar cr[],PetscScalar ci[], int *ierr)
{
CHKFORTRANNULLOBJECT(rg);
CHKFORTRANNULLSCALAR(cr);
CHKFORTRANNULLSCALAR(ci);
*ierr = RGComputeContour(
	(RG)PetscToPointer((rg) ),*n,cr,ci);
}
SLEPC_EXTERN void  rgcomputeboundingbox_(RG rg,PetscReal *a,PetscReal *b,PetscReal *c,PetscReal *d, int *ierr)
{
CHKFORTRANNULLOBJECT(rg);
CHKFORTRANNULLREAL(a);
CHKFORTRANNULLREAL(b);
CHKFORTRANNULLREAL(c);
CHKFORTRANNULLREAL(d);
*ierr = RGComputeBoundingBox(
	(RG)PetscToPointer((rg) ),a,b,c,d);
}
SLEPC_EXTERN void  rgcomputequadrature_(RG rg,RGQuadRule *quad,PetscInt *n,PetscScalar z[],PetscScalar zn[],PetscScalar w[], int *ierr)
{
CHKFORTRANNULLOBJECT(rg);
CHKFORTRANNULLSCALAR(z);
CHKFORTRANNULLSCALAR(zn);
CHKFORTRANNULLSCALAR(w);
*ierr = RGComputeQuadrature(
	(RG)PetscToPointer((rg) ),*quad,*n,z,zn,w);
}
SLEPC_EXTERN void  rgsetcomplement_(RG rg,PetscBool *flg, int *ierr)
{
CHKFORTRANNULLOBJECT(rg);
*ierr = RGSetComplement(
	(RG)PetscToPointer((rg) ),*flg);
}
SLEPC_EXTERN void  rggetcomplement_(RG rg,PetscBool *flg, int *ierr)
{
CHKFORTRANNULLOBJECT(rg);
*ierr = RGGetComplement(
	(RG)PetscToPointer((rg) ),flg);
}
SLEPC_EXTERN void  rgsetscale_(RG rg,PetscReal *sfactor, int *ierr)
{
CHKFORTRANNULLOBJECT(rg);
*ierr = RGSetScale(
	(RG)PetscToPointer((rg) ),*sfactor);
}
SLEPC_EXTERN void  rggetscale_(RG rg,PetscReal *sfactor, int *ierr)
{
CHKFORTRANNULLOBJECT(rg);
CHKFORTRANNULLREAL(sfactor);
*ierr = RGGetScale(
	(RG)PetscToPointer((rg) ),sfactor);
}
SLEPC_EXTERN void  rgpushscale_(RG rg,PetscReal *sfactor, int *ierr)
{
CHKFORTRANNULLOBJECT(rg);
*ierr = RGPushScale(
	(RG)PetscToPointer((rg) ),*sfactor);
}
SLEPC_EXTERN void  rgpopscale_(RG rg, int *ierr)
{
CHKFORTRANNULLOBJECT(rg);
*ierr = RGPopScale(
	(RG)PetscToPointer((rg) ));
}
SLEPC_EXTERN void  rgdestroy_(RG *rg, int *ierr)
{
PETSC_FORTRAN_OBJECT_F_DESTROYED_TO_C_NULL(rg);
 PetscBool rg_null = !*(void**) rg ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(rg);
*ierr = RGDestroy(rg);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! rg_null && !*(void**) rg) * (void **) rg = (void *)-2;
if (*ierr) return;
PETSC_FORTRAN_OBJECT_C_NULL_TO_F_DESTROYED(rg);
 }
#if defined(__cplusplus)
}
#endif
