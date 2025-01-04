#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* krylovschur.c */
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

#include "slepceps.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epskrylovschursetrestart_ EPSKRYLOVSCHURSETRESTART
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epskrylovschursetrestart_ epskrylovschursetrestart
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epskrylovschurgetrestart_ EPSKRYLOVSCHURGETRESTART
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epskrylovschurgetrestart_ epskrylovschurgetrestart
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epskrylovschursetlocking_ EPSKRYLOVSCHURSETLOCKING
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epskrylovschursetlocking_ epskrylovschursetlocking
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epskrylovschurgetlocking_ EPSKRYLOVSCHURGETLOCKING
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epskrylovschurgetlocking_ epskrylovschurgetlocking
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epskrylovschursetpartitions_ EPSKRYLOVSCHURSETPARTITIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epskrylovschursetpartitions_ epskrylovschursetpartitions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epskrylovschurgetpartitions_ EPSKRYLOVSCHURGETPARTITIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epskrylovschurgetpartitions_ epskrylovschurgetpartitions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epskrylovschursetdetectzeros_ EPSKRYLOVSCHURSETDETECTZEROS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epskrylovschursetdetectzeros_ epskrylovschursetdetectzeros
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epskrylovschurgetdetectzeros_ EPSKRYLOVSCHURGETDETECTZEROS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epskrylovschurgetdetectzeros_ epskrylovschurgetdetectzeros
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epskrylovschursetdimensions_ EPSKRYLOVSCHURSETDIMENSIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epskrylovschursetdimensions_ epskrylovschursetdimensions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epskrylovschurgetdimensions_ EPSKRYLOVSCHURGETDIMENSIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epskrylovschurgetdimensions_ epskrylovschurgetdimensions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epskrylovschursetsubintervals_ EPSKRYLOVSCHURSETSUBINTERVALS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epskrylovschursetsubintervals_ epskrylovschursetsubintervals
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epskrylovschurgetsubcomminfo_ EPSKRYLOVSCHURGETSUBCOMMINFO
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epskrylovschurgetsubcomminfo_ epskrylovschurgetsubcomminfo
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epskrylovschurgetsubcommpairs_ EPSKRYLOVSCHURGETSUBCOMMPAIRS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epskrylovschurgetsubcommpairs_ epskrylovschurgetsubcommpairs
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epskrylovschurgetsubcommmats_ EPSKRYLOVSCHURGETSUBCOMMMATS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epskrylovschurgetsubcommmats_ epskrylovschurgetsubcommmats
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epskrylovschurupdatesubcommmats_ EPSKRYLOVSCHURUPDATESUBCOMMMATS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epskrylovschurupdatesubcommmats_ epskrylovschurupdatesubcommmats
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epskrylovschurgetksp_ EPSKRYLOVSCHURGETKSP
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epskrylovschurgetksp_ epskrylovschurgetksp
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epskrylovschursetbsetype_ EPSKRYLOVSCHURSETBSETYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epskrylovschursetbsetype_ epskrylovschursetbsetype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define epskrylovschurgetbsetype_ EPSKRYLOVSCHURGETBSETYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define epskrylovschurgetbsetype_ epskrylovschurgetbsetype
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  epskrylovschursetrestart_(EPS eps,PetscReal *keep, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSKrylovSchurSetRestart(
	(EPS)PetscToPointer((eps) ),*keep);
}
SLEPC_EXTERN void  epskrylovschurgetrestart_(EPS eps,PetscReal *keep, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLREAL(keep);
*ierr = EPSKrylovSchurGetRestart(
	(EPS)PetscToPointer((eps) ),keep);
}
SLEPC_EXTERN void  epskrylovschursetlocking_(EPS eps,PetscBool *lock, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSKrylovSchurSetLocking(
	(EPS)PetscToPointer((eps) ),*lock);
}
SLEPC_EXTERN void  epskrylovschurgetlocking_(EPS eps,PetscBool *lock, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSKrylovSchurGetLocking(
	(EPS)PetscToPointer((eps) ),lock);
}
SLEPC_EXTERN void  epskrylovschursetpartitions_(EPS eps,PetscInt *npart, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSKrylovSchurSetPartitions(
	(EPS)PetscToPointer((eps) ),*npart);
}
SLEPC_EXTERN void  epskrylovschurgetpartitions_(EPS eps,PetscInt *npart, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLINTEGER(npart);
*ierr = EPSKrylovSchurGetPartitions(
	(EPS)PetscToPointer((eps) ),npart);
}
SLEPC_EXTERN void  epskrylovschursetdetectzeros_(EPS eps,PetscBool *detect, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSKrylovSchurSetDetectZeros(
	(EPS)PetscToPointer((eps) ),*detect);
}
SLEPC_EXTERN void  epskrylovschurgetdetectzeros_(EPS eps,PetscBool *detect, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSKrylovSchurGetDetectZeros(
	(EPS)PetscToPointer((eps) ),detect);
}
SLEPC_EXTERN void  epskrylovschursetdimensions_(EPS eps,PetscInt *nev,PetscInt *ncv,PetscInt *mpd, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSKrylovSchurSetDimensions(
	(EPS)PetscToPointer((eps) ),*nev,*ncv,*mpd);
}
SLEPC_EXTERN void  epskrylovschurgetdimensions_(EPS eps,PetscInt *nev,PetscInt *ncv,PetscInt *mpd, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLINTEGER(nev);
CHKFORTRANNULLINTEGER(ncv);
CHKFORTRANNULLINTEGER(mpd);
*ierr = EPSKrylovSchurGetDimensions(
	(EPS)PetscToPointer((eps) ),nev,ncv,mpd);
}
SLEPC_EXTERN void  epskrylovschursetsubintervals_(EPS eps,PetscReal subint[], int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLREAL(subint);
*ierr = EPSKrylovSchurSetSubintervals(
	(EPS)PetscToPointer((eps) ),subint);
}
SLEPC_EXTERN void  epskrylovschurgetsubcomminfo_(EPS eps,PetscInt *k,PetscInt *n,Vec *v, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLINTEGER(k);
CHKFORTRANNULLINTEGER(n);
PetscBool v_null = !*(void**) v ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(v);
*ierr = EPSKrylovSchurGetSubcommInfo(
	(EPS)PetscToPointer((eps) ),k,n,v);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! v_null && !*(void**) v) * (void **) v = (void *)-2;
}
SLEPC_EXTERN void  epskrylovschurgetsubcommpairs_(EPS eps,PetscInt *i,PetscScalar *eig,Vec v, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLSCALAR(eig);
CHKFORTRANNULLOBJECT(v);
*ierr = EPSKrylovSchurGetSubcommPairs(
	(EPS)PetscToPointer((eps) ),*i,eig,
	(Vec)PetscToPointer((v) ));
}
SLEPC_EXTERN void  epskrylovschurgetsubcommmats_(EPS eps,Mat *A,Mat *B, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
PetscBool A_null = !*(void**) A ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(A);
PetscBool B_null = !*(void**) B ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(B);
*ierr = EPSKrylovSchurGetSubcommMats(
	(EPS)PetscToPointer((eps) ),A,B);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! A_null && !*(void**) A) * (void **) A = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! B_null && !*(void**) B) * (void **) B = (void *)-2;
}
SLEPC_EXTERN void  epskrylovschurupdatesubcommmats_(EPS eps,PetscScalar *s,PetscScalar *a,Mat Au,PetscScalar *t,PetscScalar *b,Mat Bu,MatStructure *str,PetscBool *globalup, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
CHKFORTRANNULLOBJECT(Au);
CHKFORTRANNULLOBJECT(Bu);
*ierr = EPSKrylovSchurUpdateSubcommMats(
	(EPS)PetscToPointer((eps) ),*s,*a,
	(Mat)PetscToPointer((Au) ),*t,*b,
	(Mat)PetscToPointer((Bu) ),*str,*globalup);
}
SLEPC_EXTERN void  epskrylovschurgetksp_(EPS eps,KSP *ksp, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
PetscBool ksp_null = !*(void**) ksp ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(ksp);
*ierr = EPSKrylovSchurGetKSP(
	(EPS)PetscToPointer((eps) ),ksp);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! ksp_null && !*(void**) ksp) * (void **) ksp = (void *)-2;
}
SLEPC_EXTERN void  epskrylovschursetbsetype_(EPS eps,EPSKrylovSchurBSEType *bse, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSKrylovSchurSetBSEType(
	(EPS)PetscToPointer((eps) ),*bse);
}
SLEPC_EXTERN void  epskrylovschurgetbsetype_(EPS eps,EPSKrylovSchurBSEType *bse, int *ierr)
{
CHKFORTRANNULLOBJECT(eps);
*ierr = EPSKrylovSchurGetBSEType(
	(EPS)PetscToPointer((eps) ),bse);
}
#if defined(__cplusplus)
}
#endif
